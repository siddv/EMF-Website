from flask import request
from flask_login import current_user
from flask_restful import Resource, abort

from . import api
from main import db
from models.cfp import Proposal


class Favourite(Resource):
    def get(self, proposal_id):
        if not current_user.is_authenticated:
            abort(401)

        proposal = Proposal.query.get_or_404(proposal_id)
        current_state = proposal in current_user.favourites

        return {
            "is_favourite": current_state,
        }


    def put(self, proposal_id):
        """ Put with no data to toggle """
        if not current_user.is_authenticated:
            abort(401)

        proposal = Proposal.query.get_or_404(proposal_id)
        current_state = proposal in current_user.favourites

        data = request.get_json()
        if data.get('state') is not None:
            new_state = bool(data['state'])
        else:
            new_state = not current_state

        if new_state and not current_state:
            current_user.favourites.append(proposal)
        elif current_state and not new_state:
            current_user.favourites.remove(proposal)

        db.session.commit()

        return {
            "is_favourite": new_state,
        }


api.add_resource(Favourite, "/proposal/<int:proposal_id>/favourite")

