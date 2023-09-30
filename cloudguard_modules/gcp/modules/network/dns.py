from google.cloud import dns


class CloudDNS:
    def __init__(self,project_id:str):
        self.project_id = project_id
        self.client = dns.Client(project=self.project_id)

    def get_all_records(self) -> dict:
        zones = self.client.list_zones()
        all_records_map = {}

        for zone in zones:
            all_records_map[zone.name] = []
            records = zone.list_resource_record_sets()
            for record in records:
                record_map = {}
                record_map["name"] = record.name
                record_map["type"] = record.record_type
                record_map["data"] = record.rrdatas
                all_records_map[zone.name].append(record_map)
        return all_records_map
        

    def get_zone_records(self, zone_name:str) -> list:
        return self.get_all_records()[zone_name]


    def get_zone_records_by_type(self,zone_name:str, record_type:str) -> list:
        zone_records_by_type = []
        zone_records = self.get_zone_records(zone_name)
        for zone_record in zone_records:
            if zone_record["type"] == record_type:
                zone_records_by_type.append(zone_record)
        return zone_records_by_type


    def get_zone_records_by_name(self,zone_name:str, record_name:str) -> list:
        zone_records_by_name = []
        zone_records = self.get_zone_records(zone_name)
        for zone_record in zone_records:
            if zone_record["name"] == record_name:
                zone_records_by_name.append(zone_record)
        return zone_records_by_name
        

 