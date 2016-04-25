class User(object):
    def __init__(self, wrts):
        self.wrts = wrts

    def convert_raw(wrts, raw):
        obj = User(wrts)
        obj.full_name = raw["full_name"]
        obj.first_name = raw["first_name"]
        obj.last_name = raw["last_name"]
        obj.birthday = raw["birthday"]
        obj.gender = raw["gender"]
        obj.description = raw["description"]
        obj.phone = raw["phone"]
        obj.email = raw["email"]
        obj.zipcode = raw["zipcode"]
        obj.street = raw["street"]
        obj.house_number = raw["house_number"]
        obj.confirmed = raw["confirmed"]
        obj.last_seen_on = raw["last_seen_on"]
        obj.sign_in_count = raw["sign_in_count"]
        obj.configuration = raw["configuration"]  # TODO:fix json response
        obj.username = raw["username"]
        obj.lists = raw["lists"]  # TODO:fix json response
        obj.age = raw["age"]
        obj.age_range = raw["age_range"]
        obj.school_association = raw["school_association"]
        obj.education_level = raw["education_level"]
        obj.school_place = raw["school_place"]

        return obj
