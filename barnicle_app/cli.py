
def generate_api(config):

    template="""
from subprocess import Popen,PIPE

def os_cmd(self,cmd,route):
    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode
    if rc!=0:
        raise Exception("{0}: Exit Code {1}\\r\\nOutput:\\r\\n{2}\\r\\nError:\\r\\n{3}\\r\\n".format(route,rc,output,err))
    return output

"""

    for endpoint in configuration['endpoints']:
        route=endpoint['endpoint']
        funciton_name=endpoint['endpoint']
        if 'parameters' in endpoint:
            function_parameters=",".join(endpoint['parameters'])
            route_parameters="/"+"/".join(endpoint['parameters'])+"/"
        else:
            function_parameters=""
            route_parameters=""
        script=endpoint['script']

        route_template="""@app.route('{0}{3}')
def {1}({2}):
    retults=os_cmd('{4}','{0}')
    return results

""".format( route,
            funciton_name,
            function_parameters,
            route_parameters,
            script
        )
        template+=route_template

    return template


configuration={'endpoints': [
              {'endpoint': 'dns',
                'parameters': ['ip', 'range'],
                'script': 'dns.py'},
               {'endpoint': 'time', 'script': 'time.py'},
               {'endpoint': 'heartbeat', 'script': 'heartbeat.py'},
               {'endpoint': 'date', 'script': 'date.py'}]}

print(generate_api(configuration))

