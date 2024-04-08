# Hash table assignment

# Imports we need for our assignment
import time
from collections import defaultdict

''' Collisions are handled using separate chaining. The RegistrationHashTable class maintains an underlying list of buckets, 
where each bucket is a separate chain that holds multiple entries.'''
class RegistrationHashTable:
    # Initialize the hash table with a given size
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.state_registrations = defaultdict(list)
        self.name_registrations = defaultdict(list)

    # This will determine the index of the bucket where an entry belongs.
    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    # Insert a key-value pair into the hash table
    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)  # Update existing registration
                return
        bucket.append((key, value))  # Insert new registration

        # Add the registration to state_registrations and name_registrations
        state = value
        self.state_registrations[state].append(key)
        self.name_registrations[key].append(state)

        self.state_registrations[state].sort()  # Sort registrations for the state
        self.name_registrations[key].sort()  # Sort states for the name

    # Retrieve a key-value pair from the hash table
    def get(self, key, search_by_name = True):
        if search_by_name:
            index = self.hash_function(key)
            bucket = self.table[index]
            for existing_key, value in bucket:
                if existing_key == key:
                    return value
        else:
            return self.state_registrations.get(key)

        return None
    
    # Get all entries in the hash table
    def get_all_entries(self):
        entries = []
        for bucket in self.table:
            entries.extend(bucket)
        return entries

    # Print all entries in the hash table
    def print_all(registration_table):
        entries = registration_table.get_all_entries()
        sorted_entries = sorted(entries, key=lambda x: x[0].lower())
        for name, state in sorted_entries:
            print(f"Name: {name.capitalize()}, State: {state.upper()}")

    # Retrieve registrations by name
    def get_by_name(self, name):
        return self.name_registrations.get(name)

    # Retrieve registrations by state
    def get_by_state(self, state):
        return self.state_registrations.get(state)
    
# This function creates a hash table with a given number of buckets and returns the hash table and the time taken to create it.
def create_hash_table(num_buckets):
    start_time = time.time()
    hash_table = RegistrationHashTable(num_buckets)
    end_time = time.time()
    return hash_table, end_time - start_time

# Test with different numbers of buckets
for num_buckets in [10, 100, 1000]:
    hash_table, time_taken = create_hash_table(num_buckets)
    print(f"Number of buckets: {num_buckets}, Time taken: {time_taken} seconds")
    
''' The dataset is a list of tuples, where each tuple contains a name and a state. The dataset is used to populate the hash table. 
There is a lot of repetition in the dataset, which is intentional to test the hash table's ability to handle collisions.'''
dataset = [
("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"),
("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"),
("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"),
("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"),
("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"),
("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"),
("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"),
("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"),
("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"),
("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"),
("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"),
("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"),
("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"),
("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"),
("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"),
("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"),
("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"),
("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"),
("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"),
("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"),
("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"),
("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"),
("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"),
("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"),
("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"),
("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"),
("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"),
("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"),
("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"),
("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"),
("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"),
("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"),
("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"),
("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"),
("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"),
("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"),
("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"),
("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"),
("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"),
("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"),
("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"),
("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"),
("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"), 
("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"),
("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"),
("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"),
("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"),
("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"),
("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"),
("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"),
("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"),
("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"),
("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"),
("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"),
("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"),
("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"),
("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"),
("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"),
("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"),
("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"),
("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"),
("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"),
("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"),
("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"),
("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"),
("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"),
("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"),
("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"),
("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"),
("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"),
("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"),
("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"),
("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"),
("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"),
("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"),
("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"),
("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"),
("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"),
("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"),
("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"),
("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"),
("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"),
("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"),
("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"),
("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"),
("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), 
("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("haley", "IN"),
("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"),
("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"),
("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"),
("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"),
("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"),
("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"),
("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"),
("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"),
("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"),
("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"),
("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"),
("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"),
("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"),
("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"),
("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"),
("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"),
("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"),
("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"),
("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"),
("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"),
("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"),
("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"),
("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"),
("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"),
("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"),
("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"),
("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"),
("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"),
("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"),
("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"),
("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"),
("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"),
("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"),
("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"),
("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"),
("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"),
("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"),
("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"),
("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"),
("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"),
("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"),
("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), 
("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"),
("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"),
("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"),
("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"),
("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"),
("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"),
("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"),
("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"),
("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"),
("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"),
("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"),
("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"),
("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"),
("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"),
("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"),
("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"),
("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"),
("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"),
("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"),
("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"),
("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"),
("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"),
("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"),
("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"),
("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"),
("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"),
("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"),
("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"),
("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"),
("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"),
("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"),
("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"),
("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"),
("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"),
("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"),
("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"),
("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"),
("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"),
("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"),
("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"),
("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"),
("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"),
("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("zander", "AR"),
("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"),
("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"),
("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"),
("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"),
("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"),
("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"),
("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"),
("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"),
("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"),
("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"),
("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"),
("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"),
("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"),
("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"),
("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"),
("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"),
("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"),
("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"),
("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"),
("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"),
("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"),
("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"),
("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"),
("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"),
("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"),
("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"),
("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"),
("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"), ("jackson", "UT"),
("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"), ("olivia", "PA"),
("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"), ("taylor", "IL"),
("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"), ("yolanda", "TN"),
("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"), ("dylan", "MA"),
("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"), ("isabella", "MD"),
("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"), ("nathan", "OH"),
("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"), ("sophia", "WA"),
("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"), ("xavier", "MN"),
("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"), ("chloe", "AZ"),
("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC"), ("harrison", "NV"),
("isabella", "MD"), ("jackson", "UT"), ("kylie", "AL"), ("liam", "DE"), ("madison", "HI"),
("nathan", "OH"), ("olivia", "PA"), ("parker", "TX"), ("quinn", "CA"), ("riley", "FL"),
("sophia", "WA"), ("taylor", "IL"), ("ulrich", "GA"), ("violet", "MI"), ("william", "NC"),
("xavier", "MN"), ("yolanda", "TN"), ("zachary", "WI"), ("alice", "VA"), ("brandon", "OR"),
("chloe", "AZ"), ("dylan", "MA"), ("emily", "CO"), ("finn", "NY"), ("grace", "SC")
]

# Start timing how long it takes to execute hash table operations
start_time = time.time()

# Example usage:
registration_table = RegistrationHashTable(3440)

# Inserting registrations into the hash table
for registration in dataset:
    registration_table.insert(registration[0], registration[1])

# Printing all registrations in the hash table
RegistrationHashTable.print_all(registration_table)

# Finding a particular registration for testing
search_key = "alice"
result = registration_table.get(search_key)
if result:
    print(f"Registration for {search_key} found: {result}")
else:
    print(f"Registration for {search_key} not found.")

# End timing how long it takes to execute hash table operations
end_time = time.time()
runtime = end_time - start_time
print(f"Runtime: {runtime} seconds")

# User menu
while True:
    print("Menu:")
    print("1. Search by Name")
    print("2. Search by State")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    # Search by hash table name
    if choice == "1":
        name = input("Enter the name to search: ")
        registrations = registration_table.get_by_name(name)
        if registrations:
            print(f"Registrations for Name: {name}")
            for state in registrations:
                print(f"State: {state}")
        else:
            print(f"No registrations found for Name: {name}")

    # Search by hash table state
    elif choice == "2":
        state = input("Enter the state to search: ")
        registrations = registration_table.get_by_state(state)
        if registrations:
            print(f"Registrations for State: {state}")
            for name in registrations:
                print(f"Name: {name}")
        else:
            print(f"No registrations found for State: {state}")

    # Exit the program
    elif choice == "3":
        break

    else:
        print("Invalid choice. Please try again.")