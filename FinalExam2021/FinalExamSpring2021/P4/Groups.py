
#TODO: IMPLEMENT THE CLASS GroupedMembers

class GroupedMembers:
    def __init__(self):
        self.member_dict = {}
        self.group_dict = {}
    
    def add_member(self, group_key, name_key):
        if group_key in self.group_dict:
            self.group_dict[group_key].append(name_key)
        else:  
            self.group_dict[group_key] = [name_key]
        self.member_dict[name_key] = group_key
    
    def group_list(self, group_key):
        if group_key not in self.group_dict:
            return []
        else:
            return self.group_dict[group_key]
    
    def member_group(self, member_key):
        if member_key not in self.member_dict:
            return None
        else:
            return self.member_dict[member_key]
    
    def other_members_in_group(self, name_key):
        return self.group_dict[self.member_dict[name_key]]

if __name__ == "__main__":
    gm = GroupedMembers()
    gm.add_member("G1", "maria")
    gm.add_member("G1", "lars")
    gm.add_member("G2", "celia")
    gm.add_member("G1", "dagny")
    gm.add_member("G3", "christian")
    gm.add_member("G3", "edilon")
    gm.add_member("G2", "sunna")
    gm.add_member("G4", "larus")
    gm.add_member("G4", "constantin")

    print(gm.group_list("G1"))
    print(gm.group_list("G2"))
    print(gm.group_list("G3"))
    print(gm.group_list("G4"))

    print(gm.member_group("maria"))
    print(gm.member_group("lars"))
    print(gm.member_group("celia"))
    print(gm.member_group("dagny"))
    print(gm.member_group("christian"))
    print(gm.member_group("edilon"))
    print(gm.member_group("sunna"))
    print(gm.member_group("larus"))
    print(gm.member_group("constantin"))

    print(gm.other_members_in_group("maria"))
    print(gm.other_members_in_group("lars"))
    print(gm.other_members_in_group("celia"))
    print(gm.other_members_in_group("dagny"))
    print(gm.other_members_in_group("christian"))
    print(gm.other_members_in_group("edilon"))
    print(gm.other_members_in_group("sunna"))
    print(gm.other_members_in_group("larus"))
    print(gm.other_members_in_group("constantin"))