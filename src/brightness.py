import sys
import os
from workflow import Workflow

# GitHub repo for self-updating
GITHUB_UPDATE_CONF = {'github_slug': 'fniephaus/alfred-brightness'}
# GitHub Issues
HELP_URL = 'https://github.com/fniephaus/alfred-brightness/issues'

# default configuration
brightness_levels = '0,20,40,60,80,100'.split(',')
show_min = False
show_max = False
value_min = 0
value_max = 100
keyword_min = 'min'
keyword_max = 'max'

# get configuration from the workflow configuration values
if 'brightness_levels' in os.environ:
    brightness_levels = os.environ['brightness_levels'].split(',')

if 'show_min' in os.environ:
    show_min = os.environ['show_min']

if 'show_max' in os.environ:
    show_max = os.environ['show_max']

if 'value_min' in os.environ and os.environ['value_min'].isdigit() and int(os.environ['value_min']) >= 0:
    value_min = int(os.environ['value_min'])

if 'value_max' in os.environ and os.environ['value_max'].isdigit() and int(os.environ['value_max']) <= 100:
    value_max = int(os.environ['value_max'])

if 'keyword_min' in os.environ:
    keyword_min = os.environ['keyword_min']

if 'keyword_max' in os.environ:
    keyword_max = os.environ['keyword_max']

def main(wf):
    user_input = wf.args[0]
    error = 'Enter value between 0 and 100'

    if show_min == 'true':
        error += (', ' if show_max == 'true' else ' or ') + '"%s"' % keyword_min

    if show_max == 'true':
        error += (', or ' if show_min == 'true' else ' or ') + '"%s"' % keyword_max

    if user_input != '' and user_input != keyword_min and user_input != keyword_max:
        try:
            if int(user_input) <= 100 and int(user_input) >= 0:
                wf.add_item('%s%%' % user_input,
                            arg='%s' % (int(user_input) / 100.0), valid=True)
            else:
                wf.add_item(error)
        except ValueError:
            wf.add_item(error)

    if show_min == 'true':
        wf.add_item('%s (%s%%)' % (keyword_min, value_min),
                    arg='%s' % (value_min / 100.0),
                    valid=True)

    if show_max == 'true':
        wf.add_item('%s (%s%%)' % (keyword_max, value_max),
                    arg='%s' % (value_max / 100.0),
                    valid=True)

    for i in brightness_levels:
        if i.isdigit():
            wf.add_item('%s%%' % i, arg='%s' % (int(i) / 100.0), valid=True)

    try:
        current_value = os.popen('./brightness').readline()
        current = int(100 * float(current_value))
        wf.add_item('Current brightness: %s%%' % current, valid=False)
    except ValueError:
        wf.add_item('Cannot get current brightness')

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow(update_settings=GITHUB_UPDATE_CONF, help_url=HELP_URL)
    sys.exit(wf.run(main))
