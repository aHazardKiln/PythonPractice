'''Token bucket'''
'''Create a request throttler which throttles M requests in N seconds
Here the simplest algorithm, if you want just to drop messages when they arrive too quickly (instead of queuing them,
which makes sense because the queue might get arbitrarily large):

There are no datastructures, timers etc. in this solution and it works cleanly :) To see this, 'allowance' grows at speed 5/8 units per seconds at most,
                                                                                                                                                   i.e. at most five units per eight seconds. Every message that is forwarded deducts one unit, so you can't send more than five messages per every eight seconds.

Note that rate should be an integer, i.e. without non-zero decimal part, or the algorithm won't work correctly (actual rate will not be rate/per).
E.g. rate=0.; per=1.0; does not work because allowance will never grow to 1.0. But rate=1.0; per=2.0; works fine.
That is a standard algorithm—it's a token bucket, without queue. The bucket is allowance.
The bucket size is rate. The allowance += … line is an optimization of adding a token every rate ÷ per seconds.

'''
rate = 5.0; // unit: messages
per  = 8.0; // unit: seconds
allowance = rate; // unit: messages
last_check = now(); // floating-point, e.g. usec accuracy. Unit: seconds

when (message_received):
current = now();
time_passed = current - last_check;
last_check = current;
allowance += time_passed * (rate / per);
if (allowance > rate):
    allowance = rate; // throttle
if (allowance < 1.0):
    discard_message();
else:
    forward_message();
    allowance -= 1.0;
