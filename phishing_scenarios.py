def generate_scenario(department):
    if department == 'HR':
        return "Please review the attached HR policy update document."
    elif department == 'IT':
        return "Security Alert: Your system needs an urgent update. Click here to update now."
    elif department == 'Finance':
        return "Invoice attached for your review. Please process the payment by end of day."
    elif department == 'Marketing':
        return "Your campaign needs immediate attention. Click here to review the details."
    elif department == 'Sales':
        return "New sales lead generated. Click here to view the lead details."
    else:
        return "General phishing scenario."
