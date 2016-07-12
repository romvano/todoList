$( function() {
    $( 'form.js-do_undo' ).submit( function( e ) {
        e.preventDefault();
    } );
    $( "input.js-do_undo" ).on( "change", function() {
        var self = $( this );
        $.ajax( {
            url: '/list/do_undo/',
            type: 'post',
            data: $( this ).parent().serialize(),
            success: function( resp ) {
                if( resp == 0 ) {
                    $( '.js-note_deadline:eq(' + self.index( 'input.js-do_undo' ) + ')' ).toggleClass( 'note-done' );
                    $( '.js-note_text:eq(' + self.index( 'input.js-do_undo' ) + ')' ).toggleClass( 'note-done' );
                } else {
                    alert( resp );
                }
            },
            error: function( resp ) {
                if( resp == '<h1>403 Forbidden</h1>' ) {
                    alert( 'Incorrect user!' );
                }
            },
        } );
    } );
} );
