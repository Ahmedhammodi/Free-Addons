# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def write(self, values):
        result = super(StockPicking, self).write(values)
        count = 1
        for line in self.move_ids_without_package:
            line.line_sequence = count
            count += 1
        count2 = 1
        for line in self.move_line_ids_without_package:
            line.line_sequence = count2
            count2 += 1
        return result

    @api.model
    def create(self, vals):
        # if 'move_ids_without_package' in vals.keys():
        #     counter = 1
        #     print(counter)
        #     for line in vals['move_ids_without_package']:
        #         line[2]['line_sequence'] = counter -2
        #         counter += 1

        if 'move_line_ids_without_package' in vals.keys():
            count2 = 1
            for line in vals['move_line_ids_without_package']:
                line[2]['line_sequence'] = count2
                count2 += 1
        result = super(StockPicking, self).create(vals)
        counter = 1
        for line in result.move_ids_without_package:
            if line._origin:
                line._origin.line_sequence = counter
                counter +=1
        return result
    total_quantities = fields.Float(
        string='Total Quantities',
        required=False, compute='_compute_total_quantity', store=True)
    total_detailed_quantities = fields.Float(
        string='Total Detailed Quantities',
        required=False, compute='_compute_total_detailed_quantity', store=True)

    @api.depends('move_ids_without_package.product_uom_qty', 'move_ids_without_package')
    @api.onchange('move_ids_without_package')
    def _compute_total_quantity(self):
        for picking in self:
            total_qty = 0
            for line in picking.move_ids_without_package:
                if line._origin:
                    total_qty += line.product_uom_qty

            picking.total_quantities = total_qty

    @api.depends('move_line_ids_without_package.qty_done', 'move_line_ids_without_package')
    def _compute_total_detailed_quantity(self):
        for picking in self:
            total_qty = 0
            for line in picking.move_line_ids_without_package:
                total_qty += line.qty_done
            picking.total_detailed_quantities = total_qty

    total_line_count = fields.Integer(
        string='',
        required=False, compute='_compute_total_quantity_lines',store=True)
    total_line_detailed_count = fields.Integer(
        string='Total Detailed Lines Count',
        required=False, compute='_compute_total_detailed_quantity_lines', store=True)

    @api.depends('move_line_ids_without_package')
    def _compute_total_detailed_quantity_lines(self):
        for picking in self:
            picking.total_line_detailed_count = len(picking.move_line_ids_without_package)

    @api.depends('move_ids_without_package')
    def _compute_total_quantity_lines(self):
        for picking in self:
            count = 0
            for line in picking.move_ids_without_package:
                if line._origin:
                    count += 1
            picking.total_line_count = count


class StockMove(models.Model):
    _inherit = 'stock.move'

    line_sequence = fields.Char(
        string='No',
        required=False, readonly=1)


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    line_sequence = fields.Char(
        string='No',
        required=False, readonly=1)

