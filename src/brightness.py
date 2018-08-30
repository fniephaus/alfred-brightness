import sys
import os
from workflow import Workflow

# GitHub repo for self-updating
GITHUB_UPDATE_CONF = {'github_slug': 'fniephaus/alfred-brightness'}
# GitHub Issues
HELP_URL = 'https://github.com/fniephaus/alfred-brightness/issues'

# configuration values
brightness_levels = [int(x) for x in os.environ.get('brightness_levels', '0,20,40,60,80,100').split(',')]
show_min = os.environ.get('show_min') == 'true'
show_max = os.environ.get('show_max') == 'true'
value_min = max(0, int(os.environ.get('value_min', 0)))
value_max = min(100, int(os.environ.get('value_max', 100)))
keyword_min = os.environ.get('keyword_min', 'min')
keyword_max = os.environ.get('keyword_max', 'max')

def main(wf):
    user_input = wf.args[0]
    error = 'Enter value between 0 and 100'

    if show_min:
        error += ' or "%s"' % keyword_min

    if show_max:
        error += ' or "%s"' % keyword_max

    if user_input != '' and user_input != keyword_min and user_input != keyword_max:
        try:
            if int(user_input) <= 100 and int(user_input) >= 0:
                wf.add_item('%s%%' % user_input,
                            arg='%s' % (int(user_input) / 100.0), valid=True)
            else:
                wf.add_item(error)
        except ValueError:
            wf.add_item(error)

    if show_min:
        wf.add_item('%s (%s%%)' % (keyword_min, value_min),
                    arg='%s' % (value_min / 100.0),
                    valid=True)

    if show_max:
        wf.add_item('%s (%s%%)' % (keyword_max, value_max),
                    arg='%s' % (value_max / 100.0),
                    valid=True)

    for i in brightness_levels:
        if i >= 0:
            wf.add_item('%s%%' % i, arg='%s' % (i / 100.0), valid=True)

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
