try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    print('This would only run if no exception occurs.')
finally:
    print('This would be printed in every case.')

