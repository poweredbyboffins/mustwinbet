import json
from django.template import RequestContext
from django.shortcuts import render_to_response
from mwb.models import Games
def index(request):
    context = RequestContext(request)
    #games_list = Games.objects.all()
    games_list = Games.objects.raw("select id, replace(lower(hometeam),' ','') as hometeam,replace(lower(awayteam),' ','') as awayteam,winprob,drawprob,loseprob,gamedate from games order by id") 
    games_dict = {'gameinfo' : games_list }
    return render_to_response('mwb/index.html', games_dict, context)
    #return render_to_response('mwb/index.html', {"obj_as_json": json.dumps(games_dict)})

