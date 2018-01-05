"""Modulo de controle do jenkins"""

import getpass

from jenkinsapi.jenkins import Jenkins


def login():
    """Efetua o login, retornando usuario e senha"""
    user = input("Login [%s]: " % getpass.getuser())
    if not user:
        user = getpass.getuser()

    return user, getpass.getpass('Password:')


def get_server_instance(username, password):
    """Get Jenkins instance"""
    jenkins_url = 'http://192.168.1.110:8080'
    server = Jenkins(jenkins_url, username, password)
    return server


def get_job_details(server):
    """Get job details of each job that is running on the Jenkins instance"""
    # Refer Example #1 for definition of function 'get_server_instance'
    for j in server.get_jobs():
        job_instance = server.get_job(j[0])
        print('Job Name:%s' % (job_instance.name))
        print('Job Description:%s' % (job_instance.get_description()))
        print('Is Job running:%s' % (job_instance.is_running()))
        print('Is Job enabled:%s' % (job_instance.is_enabled()))


def list_all(filtro, server):
    jobs = []
    for j in server.get_jobs():
        job_instance = server.get_job(j[0])
        full_name = job_instance._data['fullName']
        if full_name.startswith(filtro) and not jobs.__contains__(full_name):
            jobs.append(full_name)
    print(jobs)

def exibir_opcoes():
    comando = input('Digite um comando:\nlistar\nsair\n\n')
    if(comando=='listar'):
        list_all('teste/', server)
    return comando

if __name__ == '__main__':
    # USR, PWD = login()
    USR = 'jenkinsadmin'
    PWD = 'integracaocontinua'
    server = get_server_instance(USR, PWD)
    comando = ''
    while comando != 'sair':
        comando = exibir_opcoes()
