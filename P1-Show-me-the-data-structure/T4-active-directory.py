class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_2 = Group("subchild2")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child_2.add_user("sub_child_2")

child.add_group(sub_child)
child.add_group(sub_child_2)
parent.add_group(child)

child.add_user("child_user")

def deeper_group_search(user, group, status):
    
    if user in group.get_users():
        return True
    if not group.get_groups():
        return False
    else:
        for grp in group.get_groups():
            status = deeper_group_search(user, grp, status) or status
    return status


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return deeper_group_search(user, group, False)

    if user in group.get_users():
        return True


print(is_user_in_group("sub_child_user", parent))
print(is_user_in_group("user", parent))
print(is_user_in_group("child_user", parent))
print(is_user_in_group("sub_child_2", parent))
print(is_user_in_group("", parent))