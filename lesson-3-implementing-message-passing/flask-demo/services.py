from .enums import Status

def retrieve_orders():
    """
    This is a stubbed method of retrieving multiple resources. It doesn't do anything.
    """
    return [
        {
            "order_id": 1,
            "created_by": "justin",
            "status": Status.Completed.value,
            "created_at": "2020-09-28T08:56:44",
            "equipment": [
                "KEYBOARD"
            ]
        },
        {
            "order_id": 2,
            "created_by": "tom",
            "status": Status.Queued.value,
            "created_at": "2020-09-28T09:56:44",
            "equipment": [
               "MOUSE",
               "WEBCAM"
            ]
        }
    ]


def create_order(body):
    # do stuff to process the data
    return body
