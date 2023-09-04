
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # Initialize with the specified initial members
        self._members = [
            {
                "id": 1,  
                "first_name": "John",
                "last_name": "Jackson",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "Jane",
                "last_name": "Jackson",
                "age": 5,
                "lucky_numbers": [1]
            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "last_name": "Jackson",
                "age": 35,
                "lucky_numbers": [10, 14, 32]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
    
    def get_member(self, id=None):
        if id is not None:
            # Return the member with the specified ID if found
            for member in self._members:
                if member["id"] == id:
                    return member
        # If member with the specified ID is not found, return None
        return None

    def add_member(self, member):
        # Append the new member to the list of members
        self._members.append(member)
    
    def delete_member(self, id):
        # Find the index of the member with the specified ID
        member_index = None
        for i, member in enumerate(self._members):
            if member["id"] == id:
                member_index = i
                break

        if member_index is not None:
            # Remove the member from the list if found
            deleted_member = self._members.pop(member_index)
            return deleted_member
        else:
            # Return None if the member with the given ID was not found
            return None
    
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
