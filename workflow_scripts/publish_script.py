## Script (Python) "publish_script"
##parameters=sci
# Dispatch to more easily customizable methods
object = sci.object
object.notifyPublished()

wftool = sci.getPortal().portal_workflow

# Try to make sure that conversation and contained messages are in sync
if object.portal_type == 'Message':
    parent = object.aq_inner.aq_parent
    if parent.portal_type == 'Conversation':
        try:
            if wftool.getInfoFor(parent,'review_state',None) == sci.old_state.getId():
                wftool.doActionFor(parent, sci.transition.getId())
        except:
            pass

# Publish all messages when publishing conversation
if object.portal_type == 'Conversation':
    for message in object.contentValues('Message'):
        try:
            if wftool.getInfoFor(message,'review_state',None) == sci.old_state.getId():
                wftool.doActionFor(message, sci.transition.getId())
        except:
            pass
