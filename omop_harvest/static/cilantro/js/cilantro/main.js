<<<<<<< HEAD
<<<<<<< HEAD
require({config:{tpl:{variable:"data"}}},["cilantro"],function(e){var s;return s={url:e.config.get("url"),credentials:e.config.get("credentials")},e.sessions.open(s).then(function(){var s,t;return t=[{id:"query",route:"query/",view:new e.ui.QueryWorkflow({context:this.data.contexts.session,concepts:this.data.concepts.queryable})},{id:"results",route:"results/",view:new e.ui.ResultsWorkflow({view:this.data.views.session,context:this.data.contexts.session,concepts:this.data.concepts.viewable,results:this.data.preview,exporters:this.data.exporter,queries:this.data.queries})}],e.isSupported("2.2.0")&&t.push({id:"query-load",route:"results/:query_id/",view:new e.ui.QueryLoader({queries:this.data.queries,context:this.data.contexts.session,view:this.data.views.session})}),e.isSupported("2.1.0")&&(s={queries:this.data.queries,context:this.data.contexts.session,view:this.data.views.session},e.isSupported("2.2.0")&&(s.public_queries=this.data.public_queries),t.push({id:"workspace",route:"workspace/",view:new e.ui.WorkspaceWorkflow(s)})),this.start(t)})});
=======
require({config:{tpl:{variable:"data"}},shim:{bootstrap:["jquery"],marionette:{deps:["backbone"],exports:"Marionette"},highcharts:{deps:["jquery"],exports:"Highcharts"}}},["jquery","cilantro"],function(t,e){var i={url:e.config.get("url"),credentials:e.config.get("credentials")};e.ready(function(){e.sessions.open(i).then(function(){e.panels={concept:new e.ui.ConceptPanel({collection:this.data.concepts.queryable}),context:new e.ui.ContextPanel({model:this.data.contexts.session})},e.dialogs={exporter:new e.ui.ExporterDialog({exporters:this.data.exporter}),columns:new e.ui.ConceptColumnsDialog({view:this.data.views.session,concepts:this.data.concepts.viewable}),query:new e.ui.EditQueryDialog({view:this.data.views.session,context:this.data.contexts.session,collection:this.data.queries}),deleteQuery:new e.ui.DeleteQueryDialog};var i=[];t.each(e.panels,function(t,e){e.render(),i.push(e.el)}),t.each(e.dialogs,function(t,e){e.render(),i.push(e.el)});var n=t(e.config.get("main"));n.append.apply(n,i),e.workflows={query:new e.ui.QueryWorkflow({context:this.data.contexts.session,concepts:this.data.concepts.queryable}),results:new e.ui.ResultsWorkflow({view:this.data.views.session,results:this.data.preview})};var s=[{id:"query",route:"query/",view:e.workflows.query},{id:"results",route:"results/",view:e.workflows.results}];e.isSupported("2.1.0")&&(e.workflows.workspace=new e.ui.WorkspaceWorkflow({queries:this.data.queries,context:this.data.contexts.session,view:this.data.views.session,public_queries:this.data.public_queries}),s.push({id:"workspace",route:"workspace/",view:e.workflows.workspace})),e.isSupported("2.2.0")&&(e.workflows.queryload=new e.ui.QueryLoader({queries:this.data.queries,context:this.data.contexts.session,view:this.data.views.session}),s.push({id:"query-load",route:"results/:query_id/",view:e.workflows.queryload})),this.start(s)})})});
//@ sourceMappingURL=main.js.map
>>>>>>> 0e24556... Adding Containerization (Docker) and Subfolder for Continuous Integration and Deployment (CID)
=======
require({config:{tpl:{variable:"data"}},shim:{bootstrap:["jquery"],marionette:{deps:["backbone"],exports:"Marionette"},highcharts:{deps:["jquery"],exports:"Highcharts"}}},["jquery","cilantro"],function(t,e){var i={url:e.config.get("url"),credentials:e.config.get("credentials")};e.ready(function(){e.sessions.open(i).then(function(){e.panels={concept:new e.ui.ConceptPanel({collection:this.data.concepts.queryable}),context:new e.ui.ContextPanel({model:this.data.contexts.session})},e.dialogs={exporter:new e.ui.ExporterDialog({exporters:this.data.exporter}),columns:new e.ui.ConceptColumnsDialog({view:this.data.views.session,concepts:this.data.concepts.viewable}),query:new e.ui.EditQueryDialog({view:this.data.views.session,context:this.data.contexts.session,collection:this.data.queries}),deleteQuery:new e.ui.DeleteQueryDialog};var i=[];t.each(e.panels,function(t,e){e.render(),i.push(e.el)}),t.each(e.dialogs,function(t,e){e.render(),i.push(e.el)});var n=t(e.config.get("main"));n.append.apply(n,i),e.workflows={query:new e.ui.QueryWorkflow({context:this.data.contexts.session,concepts:this.data.concepts.queryable}),results:new e.ui.ResultsWorkflow({view:this.data.views.session,results:this.data.preview})};var s=[{id:"query",route:"query/",view:e.workflows.query},{id:"results",route:"results/",view:e.workflows.results}];e.isSupported("2.1.0")&&(e.workflows.workspace=new e.ui.WorkspaceWorkflow({queries:this.data.queries,context:this.data.contexts.session,view:this.data.views.session,public_queries:this.data.public_queries}),s.push({id:"workspace",route:"workspace/",view:e.workflows.workspace})),e.isSupported("2.2.0")&&(e.workflows.queryload=new e.ui.QueryLoader({queries:this.data.queries,context:this.data.contexts.session,view:this.data.views.session}),s.push({id:"query-load",route:"results/:query_id/",view:e.workflows.queryload})),this.start(s)})})});
//@ sourceMappingURL=main.js.map
>>>>>>> 3bd2d9b... Start PEDSnet development
