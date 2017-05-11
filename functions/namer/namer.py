print("start simple function")

def handle(event, context):
    print("processing event")
    print(event)
    print(context)
    return event
