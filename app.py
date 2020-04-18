from flask import Flask
from flask_restful import Resource, Api
import iosdeploy

app = Flask(__name__)
api = Api(app)


class OperationsInstall(Resource):

    def post(self, filename):
        print("app_path: " + filename)
        ret = iosdeploy.install_app(filename)
        if ret == 253:
            return {'message': "success"}
        else:
            return {'message': "failed to install the app"}


class OperationsUninstall(Resource):
    def post(self, app_id):
        ret = iosdeploy.uninstall_app(app_id)
        if ret == 0:
            return {'message': "true"}
        else:
            return {'message': "false"}


class OperationsAppStatus(Resource):
    def get(self, app_id):
        ret = iosdeploy.is_app_installed(app_id)
        if ret == 0:
            return {'message': "true"}
        else:
            return {'message': "false"}


class OperationsContainer(Resource):
    def post(self, app_id, filename):
        ret = iosdeploy.dump_document_dir(app_id, filename)
        if ret == 0:
            return {'message': "success"}
        else:
            return {'message': "failed to install the app"}


api.add_resource(OperationsInstall, '/install/<path:filename>')
api.add_resource(OperationsUninstall, '/uninstall/<string:app_id>')
api.add_resource(OperationsAppStatus, '/appstatus/<string:app_id>')
api.add_resource(OperationsContainer, '/container/<string:app_id>/<path:filename>')

app.run(port=5000)
