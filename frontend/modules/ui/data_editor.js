import { t } from '../util/locale';
import { modeBrowse } from '../modes/browse';
import { svgIcon } from '../svg/icon';

import { uiDataHeader } from './data_header';
import { uiQuickLinks } from './quick_links';
import { uiRawTagEditor } from './raw_tag_editor';
import { uiTooltipHtml } from './tooltipHtml';


export function uiDataEditor(context) {
    var dataHeader = uiDataHeader();
    var quickLinks = uiQuickLinks();
    var rawTagEditor = uiRawTagEditor(context);
    var _datum;


    function dataEditor(selection) {
        // quick links
        var choices = [{
            id: 'zoom_to',
            label: 'inspector.zoom_to.title',
            tooltip: function() {
                return uiTooltipHtml(t('inspector.zoom_to.tooltip_data'), t('inspector.zoom_to.key'));
            },
            click: function zoomTo() {
                context.mode().zoomToSelected();
            }
        }];


        var header = selection.selectAll('.header')
            .data([0]);

        var headerEnter = header.enter()
            .append('div')
            .attr('class', 'header fillL');

        headerEnter
            .append('button')
            .attr('class', 'fr data-editor-close')
            .on('click', function() {
                context.enter(modeBrowse(context));
            })
            .call(svgIcon('#iD-icon-close'));

        headerEnter
            .append('h3')
            .text(t('map_data.title'));


        var body = selection.selectAll('.body')
            .data([0]);

        body = body.enter()
            .append('div')
            .attr('class', 'body')
            .merge(body);

        var editor = body.selectAll('.data-editor')
            .data([0]);

        // enter/update
        editor.enter()
            .append('div')
            .attr('class', 'modal-section data-editor')
            .merge(editor)
            .call(dataHeader.datum(_datum))
            .call(quickLinks.choices(choices));

        var rte = body.selectAll('.raw-tag-editor')
            .data([0]);

        // enter/update
        rte.enter()
            .append('div')
            .attr('class', 'raw-tag-editor inspector-inner data-editor')
            .merge(rte)
            .call(rawTagEditor
                .expanded(true)
                .readOnlyTags([/./])
                .tags((_datum && _datum.properties) || {})
                .state('hover')
            )
            .selectAll('textarea.tag-text')
            .attr('readonly', true)
            .classed('readonly', true);
    }


    dataEditor.datum = function(val) {
        if (!arguments.length) return _datum;
        _datum = val;
        return this;
    };


    return dataEditor;
}
