from .models import Relationship

def add_relationship(self, userprofile, status):
    relationship, created = Relationship.objects.get_or_create(
        from_person=self,
        to_person=userprofile,
        status=status)
    return relationship

def remove_relationship(self, userprofile, status):
    Relationship.objects.filter(
        from_person=self,
        to_person=userprofile,
        status=status).delete()
    return

def get_relationships(self, status):
    return self.relationships.filter(
        to_people__status=status,
        to_people__from_person=self)

def get_related_to(self, status):
    return self.related_to.filter(
        from_people__status=status,
        from_people__to_person=self)

def get_following(self):
    return self.get_relationships(RELATIONSHIP_FOLLOWING)

def get_followers(self):
    return self.get_related_to(RELATIONSHIP_FOLLOWING)