import sys
import os
from workflow import Workflow

# GitHub repo for self-updating
GITHUB_UPDATE_CONF = {'github_slug': 'fniephaus/alfred-brightness'}
# GitHub Issues
HELP_URL = 'https://github.com/fniephaus/alfred-brightness/issues'


def main(wf):
    user_input = wf.args[0]
    if user_input != '':
        try:
            if int(user_input) <= 100 and int(user_input) >= 0:
                wf.add_item('%s%%' % user_input,
                            arg='%s' % (int(user_input) / 100.0), valid=True)
            else:
                wf.add_item('Enter value between 0 and 100')
        except ValueError:
            wf.add_item('Enter value between 0 and 100')

    for i in range(0, 120, 20):
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
