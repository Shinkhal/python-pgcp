class RecordNotFoundError(Exception):
    pass

class DatabaseRecord:
    def __init__(self, record_id, data):
        self.record_id = record_id
        self.data = data
        
    def __repr__(self):
        return f"Record(id={self.record_id},data={self.data})"
    
    def __str__(self):
        return f"Record(id={self.record_id},data={self.data})"
    
class ResultSetIterator:
    def __init__(self,record_list):
        self.record_list = record_list
        self.idx_counter = 0
        
    def __iter__(self):
        return self

    def __next__(self):

        if self.idx_counter >= len(self.record_list):
            raise StopIteration

        record = self.record_list[self.idx_counter]

        self.idx_counter += 1

        return record
        
class DatabaseResultSet:
    def __init__(self, record_list):
        self.record_list = record_list
        
    def __len__(self):
        return len(self.record_list)
    
    def __iter__(self):
        return ResultSetIterator(self.record_list)
        
    def __getitem__(self, key):
        if isinstance(key,int):
            try:
                return self.record_list[key]
            except IndexError:
                print("Index out of range. ")
        elif isinstance(key,str):
            try:
                for record in self.record_list:
                        if record.data["name"] == key:
                            return record
            except:
                raise  RecordNotFoundError(f'Record with name {key} not found in database')
        else:
            raise TypeError("Key must be int or str") 
        
           
# Setup records
r1 = DatabaseRecord(101, {"name": "Alice", "role": "Admin"})
r2 = DatabaseRecord(102, {"name": "Bob", "role": "User"})

results = DatabaseResultSet([r1, r2])

# 1. Length
print(len(results))  # Output: 2

# 2. Integer Indexing
print(results[0].data["role"])  # Output: Admin

# 3. String lookup
record = results["Bob"]
print(record.record_id)  # Output: 102

# 4. Iteration
for rec in results:
    print(rec.record_id)
# Output:
# 101
# 102

# 5. Missing key lookup
try:
    missing = results["Charlie"]
except RecordNotFoundError as e:
    print(e)  # Output: Record with name 'Charlie' not found in database.