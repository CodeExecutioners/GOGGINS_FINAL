/**
 * @license Copyright (c) 2003-2014, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	config.uiColor = '#AADC6E';
    config.resize_enabled = false;

    config.toolbar = 'MyToolbar';

    config.toolbar_MyToolbar = [
        ['NewPage','Preview','Ajaxsave'],
        ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Scayt'],
        ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'],
        ['Table','HorizontalRule','Smiley','SpecialChar'],
        '/',
        ['Styles','Format'],
        ['Bold','Italic','Strike'],
        ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
        ['Link','Unlink','Anchor'],
        ['Maximize','-','About']
    ];
	
	config.extraPlugins = 'ajaxsave';

};