# --
# File: bs4_connector.py
#
# --
# -----------------------------------------
# Phantom BS4 Connector python file
# -----------------------------------------

# Phantom App imports
import phantom.app as phantom
import simplejson as json
import datetime
import inspect
import ast

from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult
from bs4_consts import *
from bs4 import BeautifulSoup, SoupStrainer


def _json_fallback(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    else:
        return obj


# Define the App Class
class Bs4Connector(BaseConnector):

    def __init__(self):

        # Call the BaseConnectors init first
        super(Bs4Connector, self).__init__()

    def _get_html_text(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the data from the params to parse
        data = param[BS4_SOURCE_STRING]

        if not data:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        try:
            parsed_html = BeautifulSoup(data, 'html.parser')
            plain_text = parsed_html.get_text()
            # .encode('ascii', 'ignore')

            # self.debug_print('soup text - {}'.format(plain_text))
            action_result.add_data(plain_text)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def _get_html_urls(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the data from the params to parse
        data = param[BS4_SOURCE_STRING]
        urls = []

        if not data:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        try:
            parsed_html = BeautifulSoup(data, "html.parser")
            for link in parsed_html.find_all('a'):
                urls.append(link.get('href'))

            action_result.add_data(urls)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def _find_strings(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the data from the params to parse
        data = param[BS4_SOURCE_STRING]
        search_string = param[BS4_SEARCH_STRING]
        strings = []

        if not data:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        try:
            parsed_html = BeautifulSoup(data, "html.parser")
            for link in parsed_html.find_all():
                self.debug_print('link -- {}'.format(link.find(search_string)))
                if link.find(search_string) != -1:
                    strings.append(link)
            self.debug_print('data raw - {}'.format(parsed_html.find_all(search_string)))
            self.debug_print('strings - {}'.format(strings))
            action_result.add_data(strings)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def _get_pretty(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the data from the params to parse
        data = param[BS4_SOURCE_STRING]

        if not data:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        try:
            parsed_html = BeautifulSoup(data, "html.parser")
            pretty_data = parsed_html.prettify()
            results = {
                "pretty": pretty_data
            }
            action_result.add_data(results)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def _transform_to_table(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the data from the params to parse
        data = param[BS4_SOURCE_STRING]

        if not data:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        try:
            data = ast.literal_eval(data)
            css = "<style>\
                    table {\
                    border-collapse: separate;\
                    border-spacing: 0px;\
                    padding-bottom: 20px;\
                    }\
                    td {\
                    border: 1px solid black;\
                    text-align: left;\
                    }\
                    </style>"
            html_data = css
            self.debug_print("type - {}".format(type(data)))
            if isinstance(data, list):
                for entry in data:
                    self.debug_print("type - {}".format(type(entry)))
                    html_table = "<table>"
                    for k, v in entry.items():
                        self.debug_print("{} {}".format(k, v))
                        html_table += "<tr><td>" + k + "</td><td>" + v + "</td></tr>"
                    html_data += html_table + "</table></br>"
                self.debug_print(html_data)
            elif isinstance(data, dict):
                html_table = "<table>"
                for k, v in entry:
                    html_table += "<tr><td>" + k + "</td><td>" + v + "</td></tr>"
                html_data += html_table + "</table>"
            action_result.add_data({'table': html_data})
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def _extract_tag(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        try:
            # Create soup
            soup = BeautifulSoup(param[BS4_SOURCE_STRING], "html.parser")

            # Extract from soup
            tags = soup(param.get('tag'))
            soup_extract = tags[0].extract()

            # Convert the resulting soup to a string and add to data dictionary
            results = {
                "results": unicode(soup_extract)
            }
            action_result.add_data(results)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def _find_all(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Get the data from the params to parse
        data = param[BS4_SOURCE_STRING]
        # field = param[BS4_FIND_FIELD]

        if not data:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        try:
            parsed_html = BeautifulSoup(data, "html.parser")
            self.debug_print("html: {}".format(parsed_html.find_all('table')))
            data = parsed_html.find_all('table')
            # self.debug_print("data: {!r}".format(data))
            results = {
                "field_list": str(data)
            }
            # action_result.add_data(data)
            action_result.add_data(results)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def _remove_attributes(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        try:
            # Create list and soup
            attrib_list = [x.strip() for x in str(param[BS4_ATTRIBUTE_LIST]).split(",")]
            soup = BeautifulSoup(param[BS4_SOURCE_STRING], "html.parser")

            # Remove attribute from soup
            for tag in soup():
                for attribute in attrib_list:
                    del tag[attribute]
            results = {
               "results": unicode(soup)
            }
            action_result.add_data(results)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def _remove_tags(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        try:
            # Create list and soup
            tag_list = [x.strip() for x in str(param[BS4_TAG_LIST]).split(",")]
            soup = BeautifulSoup(param[BS4_SOURCE_STRING], "html.parser")

            # Remove tags from soup
            for target_tag in tag_list:
                for tag in soup(target_tag):
                    tag.decompose()

            results = {
               "results": unicode(soup)
            }
            action_result.add_data(results)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def _extract_tags(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        try:
            # Create list and soup
            tag_list = [x.strip() for x in str(param[BS4_TAG_LIST]).split(",")]

            soup = BeautifulSoup(param[BS4_SOURCE_STRING], "html.parser", parse_only=SoupStrainer(tag_list))

            results = {
               "results": unicode(soup)
            }
            action_result.add_data(results)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def _wrap_tag(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        try:
            # Create list and soup
            tag_list = [x.strip() for x in str(param[BS4_TAG_LIST]).split(",")]

            soup = BeautifulSoup(param[BS4_SOURCE_STRING], "html.parser", parse_only=SoupStrainer(tag_list))

            results = {
               "results": unicode(soup)
            }
            action_result.add_data(results)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def _unwrap_tag(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        try:
            # Create list and soup
            soup = BeautifulSoup(param[BS4_SOURCE_STRING], "html.parser")
            wrapped_tags = soup([x.strip() for x in str(param[BS4_TAG_LIST]).split(",")])
            for tag in wrapped_tags:
                self.debug_print("tag - {}".format(tag))
                tag.unwrap()

            results = {
               "results": unicode(soup)
            }
            action_result.add_data(results)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def handle_action(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        ret_val = phantom.APP_SUCCESS
        action = self.get_action_identifier()
        self.debug_print("action_id", self.get_action_identifier())

        if (action == "find_strings"):
            ret_val = self._find_strings(param)
        elif (action == "get_html_text"):
            ret_val = self._get_html_text(param)
        elif (action == "get_html_urls"):
            ret_val = self._get_html_urls(param)
        elif (action == "get_pretty"):
            ret_val = self._get_pretty(param)
        elif (action == "transform_to_table"):
            ret_val = self._transform_to_table(param)
        elif (action == "find_all"):
            ret_val = self._find_all(param)
        elif (action == "remove_attributes"):
            ret_val = self._remove_attributes(param)
        elif (action == "remove_tags"):
            ret_val = self._remove_tags(param)
        elif (action == "extract_tag"):
            ret_val = self._extract_tag(param)
        elif (action == "extract_tags"):
            ret_val = self._extract_tags(param)
        elif (action == "wrap_tag"):
            ret_val = self._wrap_tag(param)
        elif (action == "unwrap_tag"):
            ret_val = self._unwrap_tag(param)

        return ret_val


if __name__ == '__main__':

    import sys
    import pudb
    pudb.set_trace()

    if (len(sys.argv) < 2):
        print "No test json specified as input"
        exit(0)

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = PythonUtilitiesConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print (json.dumps(json.loads(ret_val), indent=4))

    exit(0)
