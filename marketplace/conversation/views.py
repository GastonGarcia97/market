# from django.shortcuts import render,get_object_or_404,redirect

# from item.models import Item

# from .forms import ConversationMessageForm
# from .models import Conversation
# # Create your views here.

# def new_conversation(request,item_pk):
#     item = get_object_or_404(Item, pk=item_pk)

#     if item.created_by == request.user:
#         return redirect('dashboard:index')

#     conversations= Conversation.objects.filter(item=item).filter(members__in=[request.user,])

#     if conversations:
#         pass # redirect to conversation

#     if request.method == 'POST':
#         form= ConversationMessageForm(request.POST)

#         if form.is_valid():

#             conversation= Conversation.objects.create(item=item)
#             conversation.members.add(request.user)
#             conversation.members.add(item.created_by)
#             conversation.save()

#             conversations_message=form.save(commit=False)
#             conversations_message.conversation=conversation
#             conversations_message.created_by=request.user
#             conversations_message.save()

#             return redirect('item:detail',pk=item_pk)
#     else:   
#         form= ConversationMessageForm

#     return (request,conversation/new.html,{
#         'item':item,'form':form
#         })