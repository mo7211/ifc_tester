import csv
import ifcopenshell
from ifctester import ids, reporter

class IDSGenerator:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.my_ids = ids.Ids(title="My IDS")
    
    def generate_ids_from_csv(self):
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                next(reader) 
                for row in reader:
                    self.add_specification(row)
            self.my_ids.to_xml("SampleIDS.ids")
        except Exception as e:
            print(f"An error occured: {e}")
    
    def add_specification(self, row):
        ifc_class, predefined_type, pset, prop, datatype, value = row
        my_spec = ids.Specification(name=f"Specification for {ifc_class}")
        my_spec.applicability.append(ids.Entity(name=ifc_class.upper()))
        
        property = ids.Property(
            name=prop, 
            value=value, 
            propertySet=pset, 
            datatype=datatype,
            uri="<Insert proper URI here>", 
            instructions="<Insert proper instruction here>",
            minOccurs=1,
            maxOccurs="unbounded")
        my_spec.requirements.append(property)
        self.my_ids.specifications.append(my_spec)

def main():
    # Instantiate generator with input files
    gen = IDSGenerator('requirements.csv')
    gen.generate_ids_from_csv()

if __name__ == "__main__":
    main()