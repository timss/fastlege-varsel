#!/usr/bin/env python

import dbus

def desktop(title, body="", app_name="", app_icon="",
            timeout=5000, actions=[], hints=[], replaces_id=0):
    """Shows a desktop notification using D-Bus.

    Using the freedesktop.org and D-Bus standards to display a desktop
    notification using the same code on most popular desktop environments.
    http://mueller.panopticdev.com/2011/06/create-notification-bubbles-in-python.html
    """
    try:
        bus_name    = "org.freedesktop.Notifications"
        object_path = "/org/freedesktop/Notifications"

        session_bus = dbus.SessionBus()
        obj         = session_bus.get_object(bus_name, object_path)
        interface   = dbus.Interface(obj, bus_name)

        interface.Notify(app_name, replaces_id, app_icon,
                summary, body, actions, hints, timeout)

        return True
    except: # TODO: exception e
        return False

def email(sender, recipient, subject, body,
          server, user, name, passwd):
    """Sends an e-mail notification.

    Using a specified SMTP server sends an e-mail notification.
    Could be done using a shared/public e-mail, maybe even using Gmail.
    """
    pass
