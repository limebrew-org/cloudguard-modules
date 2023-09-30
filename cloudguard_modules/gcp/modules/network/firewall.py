from googleapiclient import discovery

class Firewall:
    def __init__(self,project_id:str):
        self.project_id = project_id
        self.client = discovery.build('compute','v1')

    def get_all_firewall_rules(self):
        firewall_rules = self.client.firewalls().list(project=self.project_id).execute()
        return firewall_rules.get('items', [])