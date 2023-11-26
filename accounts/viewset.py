from django.shortcuts import get_object_or_404
from vrm.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

#-----models-----------------------------------
from accounts.models import User, Profile, Role, UserRoleMaping, Location, RoleHistory,NotificationPreference
from django.contrib.auth.models import Group
from vrm.models.course import Course
from utils.models import Language

class UserProfileViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        data = User.objects.filter(id=request.user.id).values('username', 'email', 'first_name', 'last_name', 'date_joined').first()
        profile = Profile.objects.filter(user=request.user).first()
        data['terms'] = profile.terms
        data['reference'] = profile.reference.email
        data['dob'] = profile.dob
        data['mobile'] = profile.mobile
        data['gender'] = [{'id':g[0], 'name':g[1]} for g in profile.Gender.choices if g[0]==profile.gender][0]
        data['genders'] = [{'id':g[0], 'name':g[1]} for g in profile.Gender.choices]
        data['country'] = profile.location.country
        data['state'] = profile.location.state
        data['city'] = profile.location.city
        data['pincode'] = profile.pincode
        data['professions'] = [{'id':p[0], 'name':p[1]} for p in profile.Profession.choices]
        data['profession'] = [{'id':p[0], 'name':p[1]} for p in profile.Profession.choices if p[0]==profile.profession][0] if profile.profession else data['professions'][-1]
        data['educations'] = [{'id':p[0], 'name':p[1]} for p in profile.Education.choices]
        data['education'] = [{'id':e[0], 'name':e[1]} for e in profile.Education.choices if e[0]==profile.education][0] if profile.education else data['educations'][-1]
        data['linkedIn'] = profile.linkedIn
        data['step'] = profile.step
        data['groups'] = request.user.groups.all().values_list('id', flat=True)
        data['language'] = {'id': profile.language.id, 'name':profile.language.name}
        data['about'] = profile.about
        roles = Role.objects.filter(status=True)

        k = []
        
        for role in roles:
            a = {
                'id':role.id, 'name':role.name, 'opted': False, 'activate': False, 'status': False, 'notes':'', 'history': []
            }
            role_maping = UserRoleMaping.objects.filter(user=request.user, role=role).exclude(status=UserRoleMaping.Status.REJECTED).last()
            if role_maping:
                a['opted'] = True
                a['activate'] = role_maping.active
                a['status'] = [x[1] for x in UserRoleMaping.Status.choices if x[0]==role_maping.status][0]
                a['description'] = role_maping.notes

            history = RoleHistory.objects.filter(role=role, user=request.user).values()
            q = []
            if history:
                for m in history:
                    q.append({ 'id': m.id, 'name': m.note, 'date': m.created_at })
                a['history'] = q
            k.append(a)
        data['roles'] = k

        prfs = NotificationPreference.objects.filter(user=request.user).values('email', 'sms', 'watsapp').first()
        data['preferences'] = prfs

        return Response(data)


    def post(self, request):
        userkeys = ["email", "first_name", "last_name", ] 
        profile_direct = ["terms", "reference", "dob", "mobile", "pincode",  "linkedIn", "step", 'abount']
        profile_process1 = ["gender", "country", "state", "city","profession","language",]
        data = request.data['data']
        print(data)
        userDict = {}   
        profileDict = {}
        for key, val in data.items():
            if key in userkeys: userDict[key]=val
            elif key in profile_direct: profileDict[key]=val
            elif key in profile_process1: profileDict[key]=val['id']
            elif key=='preferences':
                pass
            elif key=='roles':
                pass



        print(userDict)
        print(profileDict)
        return Response({})
    

class LocationViewset(viewsets.ViewSet):

    """
    A simple ViewSet for listing or retrieving users.
    """
    
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        context = {}
        context['locations'] = Location.objects.all().values('id', 'country', 'state', 'city')
        context['languages'] = Language.objects.all().values('id', 'name', 'code')
        
        return Response(context)

