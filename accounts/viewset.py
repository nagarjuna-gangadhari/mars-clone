from django.shortcuts import get_object_or_404
from vrm.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

#-----models-----------------------------------
from accounts.models import User, Profile, Role, UserRoleMaping, RoleHistory,NotificationPreference
from django.contrib.auth.models import Group
from taxonomy.models import Language, Location

class UserProfileViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        data = User.objects.filter(id=request.user.id).values('username', 'email', 'first_name', 'last_name', 'date_joined').first()
        profile = Profile.objects.filter(user=request.user).first()
        data['terms'] = profile.terms
        data['reference'] = profile.reference.email if profile.reference else ''
        data['dob'] = profile.dob
        data['mobile'] = profile.mobile
        data['gender'] = [{'id':g[0], 'name':g[1]} for g in profile.Gender.choices if g[0]==profile.gender][0]
        data['genders'] = [{'id':g[0], 'name':g[1]} for g in profile.Gender.choices]
        data['country'] = profile.location.country if profile.location else ''
        data['state'] = profile.location.state if profile.location else ''
        data['city'] = profile.location.city if profile.location else ''
        data['pincode'] = profile.pincode
        data['professions'] = [{'id':p[0], 'name':p[1]} for p in profile.Profession.choices]
        data['profession'] = [{'id':p[0], 'name':p[1]} for p in profile.Profession.choices if p[0]==profile.profession][0]
        data['educations'] = [{'id':p[0], 'name':p[1]} for p in profile.Education.choices]
        data['education'] = [{'id':e[0], 'name':e[1]} for e in profile.Education.choices if e[0]==profile.education][0]
        data['step'] = profile.step
        data['groups'] = request.user.groups.all().values_list('id', flat=True)
        data['language'] = {'id': profile.language.id, 'name':profile.language.name} if profile.language else {}
        data['about'] = profile.about
        data['linkedIn'] = profile.linkedIn
        roles = Role.objects.filter(status=True)

        k = []
        
        for role in roles:
            a = {
                'id':role.id, 'name':role.name, 'opted': False, 'active': False, 'status': False, 'notes':'', 'history': []
            }
            role_maping = UserRoleMaping.objects.filter(user=request.user, role=role).exclude(status=UserRoleMaping.Status.REJECTED).last()
            if role_maping:
                a['opted'] = True if role_maping.status >1 else False
                a['activate'] = role_maping.active
                a['status'] = role_maping.get_status_display()
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
        try:
            userkeys = ["email", "first_name", "last_name"] 
            profile_direct = ["terms", "reference", "dob", "mobile", "pincode",  "linkedIn", "step", 'about']
            profile_process1 = ["gender","profession","language",]
            profile_process2 = [ "country", "state", "city"]
            data = request.data['data']
            print(data)
            userDict = {}   
            profileDict = {}
            for key, val in data.items():
                if key in userkeys: userDict[key]=val
                elif key in profile_direct: profileDict[key]=val
                elif key in profile_process1: profileDict[key]=val['id']
                elif key in profile_process2:
                    profileDict['location'] = Location.objects.filter(city__contains=val['name']).first()
                    
                elif key=='preferences':
                    prefer, created = NotificationPreference.objects.get_or_create(user_id=request.user.id)
                    if val.get('email') is not None: prefer.email=val.get('email')
                    elif val.get('sms') is not None: prefer.sms=val.get('sms')
                    elif val.get('watsapp') is not None: prefer.watsapp=val.get('watsapp')
                    prefer.save()

                elif key=='roles':
                    for role in val:
                        urm, created = UserRoleMaping.objects.get_or_create(user_id=request.user.id, role_id=role['id'])
                        if not created and role.get('opted'): urm.status = UserRoleMaping.Status.OPTED
                        else: urm.status = UserRoleMaping.Status.NOT_OPTED
                        urm.save()
            if userDict: obj = User.objects.filter(id=request.user.id).update(**userDict)
            if profileDict: obj = Profile.objects.filter(user_id=request.user.id).update(**profileDict)
            print(userDict)
            print(profileDict)            
            return Response({})
        except Exception as e:
            print(e)
            return None
    

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

