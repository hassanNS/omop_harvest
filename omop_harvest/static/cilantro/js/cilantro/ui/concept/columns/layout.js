define(["jquery","underscore","backbone","marionette","../search","./available","./selected"],function(t,e,i,n,s,o,r){var a=n.ItemView.extend({className:"popover right",template:"concept/popover",initialize:function(){this.$el.css({position:"fixed",zIndex:1200,minWidth:300,minHeight:100}).hide()},serializeData:function(){var t=this.model.toJSON(),e=this.model.fields;return 0===e.length?t.description||(t.description='<i class="icon-spinner icon-spin"></i>'):1===e.length?t.description||(t.description=e.models[0].get("description")):t.fields=e.map(function(t){return t.get("name")}).join(", "),t.description||t.fields||(t.description="<em>No description is available</em>"),t},onRender:function(){0===this.model.fields.length&&(this.listenTo(this.model.fields,"reset",this.show),this.model.fields.fetch({reset:!0}))},update:function(t){this.stopListening(),this.options=t,this.model=t.model,this.show()},show:function(){this.render(),this.shown()?this.$el.stop().animate({left:this.options.left,top:this.options.top-this.$el.outerHeight()/2},200):this.$el.show().css({left:this.options.left,top:this.options.top-this.$el.outerHeight()/2}).fadeIn(200)},shown:function(){return this.$el.is(":visible")},hide:function(){this.$el.fadeOut(200)}}),l=n.Layout.extend({className:"concept-columns",template:"concept/columns/layout",events:{click:"hideDetailsPopover","click [data-action=clear]":"triggerRemoveAll"},regions:{search:".search-region",available:".available-region",selected:".selected-region"},regionViews:{search:s.ConceptSearch,available:o.AvailableColumns,selected:r.SelectedColumns},initialize:function(){if(this.data={},!(this.data.view=this.options.view))throw new Error("view required");if(!(this.data.concepts=this.options.concepts))throw new Error("concepts collection required");this.listenTo(this.data.concepts,"columns:detail",this.handleDetailsPopover),this.data.selected=new i.Collection,this.data.selected.listenTo(this.data.concepts,"columns:add",function(t){this.add(t)}),this.data.selected.on("columns:remove",function(t){this.remove(t)})},handleDetailsPopover:function(i,n){var s=this,o=t(n.currentTarget);if(clearTimeout(this._detailsDelay),"mouseover"===n.type){var r=this.popover.shown()?100:500;this._detailsDelay=e.delay(function(){s.showDetailsPopover(i,o)},r)}else"mouseout"===n.type&&(this._detailsDelay=e.delay(function(){s.hideDetailsPopover(i,o)},200))},showDetailsPopover:function(e,i){i=t(i);var n=i.offset();this.popover.update({model:e,top:n.top+i.outerHeight()/2,left:n.left+i.outerWidth()})},hideDetailsPopover:function(){this.popover&&this.popover.hide()},resetSelected:function(){this.data.selected.reset();var t=this.data.concepts;this.data.view.facets.each(function(e){var i=t.get(e.get("concept"));i&&i.trigger("columns:add",i)})},selectedToFacets:function(){var t=this;return this.data.selected.map(function(e){var i=t.data.view.facets.get(e.id);return i?i.toJSON():{concept:e.id}})},onRender:function(){this.$el.modal({show:!1});var t=new this.regionViews.search({placeholder:"Search available columns by name, description, or data value...",collection:this.data.concepts,handler:function(t,i){e.filter(t,i)}}),e=new this.regionViews.available({collapsable:!1,collection:this.data.concepts}),i=new this.regionViews.selected({collection:this.data.selected});this.search.show(t),this.available.show(e),this.selected.show(i),this.popover=new a,this.$el.append(this.popover.el),this.data.view.facets.length>0&&this.data.concepts.length?this.resetSelected():(this.listenToOnce(this.data.view.facets,"reset",this.resetSelected),this.listenToOnce(this.data.concepts,"reset",this.resetSelected))},triggerRemoveAll:function(){var t=this.data.selected.slice(0);e.each(t,function(t){t.trigger("columns:remove",t)})}});return{ConceptColumnsLayout:l}});
//@ sourceMappingURL=layout.js.map