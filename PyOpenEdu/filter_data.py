"""
    filter data table
"""
class FilterInterface():
    """
        interface for filter data.
    """
    def __init__(self, data, field, value):
        self.data = data
        self.field = field
        self.value = value

    def filter_data(self):
        pass

class filter_data_bridge():
    """
        the bridge for using filter data
    """
    def __init__(self, func):
        self._func = func

    def filter_data(self):

        filter_data_done = self._func.filter_data()

        return filter_data_done

class filter_data_extend(FilterInterface):
    """
        filter type name: extend
    """

    def filter_data(self):

        filter_data_mask = self.data[self.field].str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_accept_language(filter_data_extend):
    """
        filter type name: accept_language
    """

    def filter_data(self):

        filter_data_mask = self.data.accept_language.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_agent(filter_data_extend):
    """
        filter type name: agent
    """

    def filter_data(self):

        filter_data_mask = self.data.agent.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_context(filter_data_extend):
    """
        filter type name: context
    """

    def filter_data(self):

        filter_data_mask = self.data.context.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_event(filter_data_extend):
    """
        filter type name: event
    """

    def filter_data(self):

        filter_data_mask = self.data.event.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_event_source(filter_data_extend):
    """
        filter type name: event_source
    """

    def filter_data(self):

        filter_data_mask = self.data.event_source.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_event_type(filter_data_extend):
    """
        filter type name: event_type
    """

    def filter_data(self):

        filter_data_mask = self.data.event_type.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_host(filter_data_extend):
    """
        filter type name: host
    """

    def filter_data(self):

        filter_data_mask = self.data.host.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_ip(filter_data_extend):

    def filter_data(self):

        filter_data_mask = self.data.ip.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_name(filter_data_extend):

    def filter_data(self):

        filter_data_mask = self.data.name.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_page(filter_data_extend):

    def filter_data(self):

        filter_data_mask = self.data.page.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_referer(filter_data_extend):

    def filter_data(self):

        filter_data_mask = self.data.referer.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_session(filter_data_extend):

    def filter_data(self):

        filter_data_mask = self.data.session.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_time(filter_data_extend):

    def filter_data(self):

        filter_data_mask = self.data.time.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class filter_data_username(filter_data_extend):

    def filter_data(self):

        filter_data_mask = self.data.username.str.find(sub=self.value)

        for i in range(len(filter_data_mask)):

            if filter_data_mask[i] != -1:
                filter_data_mask[i] = True
            elif filter_data_mask[i] == -1:
                filter_data_mask[i] = False

        filter_data_done = self.data[filter_data_mask]

        filter_data_done = filter_data_done.reset_index(drop=True)

        return filter_data_done

class Filter_data():

    def __init__(self):
        pass

    def filter_data_bridge(self, func):

        filter_data = filter_data_bridge(func)
        fd = filter_data.filter_data()

        return fd

    def filter_data_accept_language(self, origin_log_data, Field_value=''):
        # data, field, value
        filter_data_done = filter_data_accept_language(origin_log_data,
                                                       'accept_language', Field_value)

        return filter_data_done

    def filter_data_agent(self, origin_log_data, Field_value=''):

        filter_data_done = filter_data_agent(origin_log_data, 'agent', Field_value)

        return filter_data_done

    def filter_data_context(self, origin_log_data, Field_value=''):

        filter_data_done = filter_data_context(origin_log_data, 'context', Field_value)

        return filter_data_done

    def filter_data_event(self, origin_log_data, Field_value=''):

        filter_data_done = filter_data_event(origin_log_data, 'event', Field_value)

        return filter_data_done

    def filter_data_event_source(self, origin_log_data, Field_value=""):

        filter_data_done = filter_data_event_source(origin_log_data, 'event_source', Field_value)

        return filter_data_done

    def filter_data_event_type(self, origin_log_data, Field_value=''):

        filter_data_done = filter_data_event_type(origin_log_data, 'event_type', Field_value)

        return filter_data_done

    def filter_data_host(self, origin_log_data, Field_value=''):

        filter_data_done = filter_data_host(origin_log_data, 'host', Field_value)

        return filter_data_done

    def filter_data_ip(self, origin_log_data, Field_value=''):

        filter_data_done = filter_data_ip(origin_log_data, 'ip', Field_value)

        return filter_data_done

    def filter_data_name(self, origin_log_data, Field_value=''):

        filter_data_done = filter_data_name(origin_log_data, 'name', Field_value)

        return filter_data_done

    def filter_data_page(self, origin_log_data, Field_value=''):

        filter_data_done = filter_data_page(origin_log_data, 'page', Field_value)

        return filter_data_done

    def filter_data_referer(self, origin_log_data, Field_value=''):

        filter_data_done = filter_data_referer(origin_log_data, 'referer', Field_value)

        return filter_data_done

    def filter_data_session(self, origin_log_data, Field_value=''):

        filter_data_done = filter_data_session(origin_log_data, 'session', Field_value)

        return filter_data_done

    def filter_data_time(self, origin_log_data, Field_value=''):

        filter_data_done = filter_data_time(origin_log_data, 'time', Field_value)

        return filter_data_done

    def filter_data_username(self, origin_log_data, Field_value=''):

        filter_data_done = filter_data_username(origin_log_data, 'username', Field_value)

        return filter_data_done
