# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)
from requests_oauthlib import OAuth2

from .resource_mapping import RESOURCE_MAPPING


class FacebookClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://graph.facebook.com/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(FacebookClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        params['auth'] = OAuth2(
            api_params.get('client_id'), token={
            'access_token': api_params.get('access_token'),
            'token_type': 'Bearer'})

        return params

    def get_iterator_list(self, response_data):
        return response_data['data']

    def get_iterator_next_request_kwargs(self,
            iterator_request_kwargs, response_data, response):
        paging = response_data.get('paging')
        if not paging:
            return
        url = paging.get('next')

        if url:
            return {'url': url}


Facebook = generate_wrapper_from_adapter(FacebookClientAdapter)
