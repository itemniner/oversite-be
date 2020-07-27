class MemberShow:
    def __init__(self, data):
        self.id = data['id']
        self.image = f"https://theunitedstates.io/images/congress/original/{data['id']}.jpg"
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.role = data['roles'][0]['title']
        self.phone = data['roles'][0]['phone']
        self.address = data['roles'][0]['office']
        self.twitter_url = self.twitter_url(data)
        self.twitter_handle = data['twitter_account']
        self.youtube = self.youtube_url(data)
        self.facebook = self.facebook_url(data)
        self.party = self.party_name(data)
        self.chamber = data['roles'][0]['chamber']
        self.state = data['roles'][0]['state']
        self.district = self.district_filter(data)
        self.website = data['url']
        self.contact_form_url = data['roles'][0]['contact_form']

    def party_name(self, party):
        if party == 'R':
          return 'Republican'
        elif party == 'D':
          return 'Democrat'
        elif party == 'I':
          return 'Independent'
        else:
          return party

    def twitter_url(self, data):
        if data['twitter_account'] == None:
          return None
        else:
          return f"https://twitter.com/{data['twitter_account']}"

    def facebook_url(self, data):
        if data['facebook_account'] == None:
          return None
        else:
          return f"https://www.facebook.com/{data['facebook_account']}"

    def youtube_url(self, data):
        if data['youtube_account'] == None:
          return None
        else:
          return f"https://www.youtube.com/user/{data['youtube_account']}"

    def district_filter(self, data):
        if data['roles'][0]['chamber'] == 'House':
          return data['roles'][0]['district']
        else:
          return None

    def serialize(self):
        return {
            'id' : self.id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'image' : self.image,
            'role' : self.role,
            'phone' : self.phone,
            'address' : self.address,
            'twitter_url' : self.twitter_url,
            'twitter_handle' : self.twitter_handle,
            'youtube' : self.youtube,
            'facebook' : self.facebook,
            'party' : self.party,
            'chamber' : self.chamber,
            'state' : self.state,
            'district' : self.district,
            'website' : self.website,
            'contact_form_url' : self.contact_form_url
        }
class MemberIndex:
    def __init__(self,
                 id,
                 first_name,
                 last_name,
                 role,
                 party):
        self.id = id
        self.image = f'https://theunitedstates.io/images/congress/original/{id}.jpg'
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.party = self.party_name(party)

    def party_name(self, party):
        if party == 'R':
          return 'Republican'
        elif party == 'D':
          return 'Democrat'
        elif party == 'I':
          return 'Independent'
        else:
          return party

    def serialize(self):
        return {
            'id': self.id,
            'image': self.image,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role,
            'party': self.party
        }
