from flask import request
from flask_restplus import Resource

from ..util.dto import InvoiceDto
from ..service.invoice_service import save_new_invoice, get_all_invoices, get_invoices_by_query, get_invoice_by_id

api = InvoiceDto.api
_invoice = InvoiceDto.invoice


@api.route('/')
class InvoiceList(Resource):
    @api.doc('list of invoices')
    @api.marshal_list_with(_invoice, envelope='data')
    def get(self):
        """List all registered patients"""
        return get_all_invoices()

    @api.response(201, 'Invoice successfully created.')
    @api.doc('create a new invoice')
    @api.expect(_invoice, validate=True)
    def post(self):
        """Creates a new Invoice """
        data = request.json
        return save_new_invoice(data=data)


@api.route('/<invoice_id>')
@api.param('invoice_id', 'The Invoice identifier')
@api.response(404, 'Invoice not found.')
class Invoice(Resource):
    @api.doc('get invoice by id')
    @api.marshal_with(_invoice)
    def get(self, invoice_id):
        """get a invoice given its identifier"""
        invoice = get_invoice_by_id(invoice_id)
        if not invoice:
            api.abort(404)
        else:
            return invoice


@api.route('/search')
@api.param('q', 'Query used for search')
class InvoiceSearch(Resource):
    @api.doc('search invoice')
    @api.marshal_list_with(_invoice, envelope='data')
    @api.response(201, 'Invoice not found')
    def get(self):
        """List of invoices who satisfy the search"""
        query = request.args.get('q', None)
        return get_invoices_by_query(query)
