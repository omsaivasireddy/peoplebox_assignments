def process_status(data):
    # Print status message based on data's status.
    status_messages = {
        'active': 'Active',
        'inactive': 'Inactive'
    }
    print(status_messages.get(data['status'], 'Unknown'))