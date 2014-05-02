import sys
import os
from workflow import Workflow


def main(wf):
    user_input = wf.args[0]
    if user_input != '':
        try:
            if int(user_input) <= 100 and int(user_input) > 0:
                wf.add_item('%s%%' % user_input, arg='%s' % (int(user_input) / 100.0), valid=True)
            else:
                wf.add_item('Enter value between 0 and 100')
        except ValueError:
            wf.add_item('Enter value between 0 and 100')

    for i in range(0,120, 20):
        wf.add_item('%s%%' % i, arg='%s' % (i / 100.0), valid=True)

    current_value = os.popen('./brightness').readline()
    wf.add_item('Current brightness: %s%%' % int(100 * float(current_value)), valid=False)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
