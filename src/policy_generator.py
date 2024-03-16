def generate_policy(principal_id, effect, resource):
    # Cria uma política IAM para autorização
    policy_document = {
        'Version': '2012-10-17',
        'Statement': [{
            'Action': 'execute-api:Invoke',
            'Effect': effect,
            'Resource': resource
        }]
    }
    return {
        'principalId': principal_id,
        'policyDocument': policy_document
    }
