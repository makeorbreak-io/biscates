function acceptProposal(proposalID) {
    var jqxhr = $.post( "/proposal", {type: 'accept',proposalID: proposalID}, function(result) {
        alert( result );
    })
    .done(function() {
        alert( "second success" );
    })
    .fail(function() {
        alert( e.toString() );
    })
    .always(function() {
        alert( "finished" );
    });
}

function rejectProposal(proposalID) {
    var jqxhr = $.post( "/proposal", {type: 'reject',proposalID: proposalID}, function() {
        alert( "success" );
    })
    .done(function() {
        alert( "second success" );
    })
    .fail(function(e) {
        alert( e.toString() );
    })
    .always(function() {
        alert( "finished" );
    });
}



$(document).ready(function () {
    $('.ui.dropdown').dropdown({
        onChange: function(){
            $('.create-task > input').removeAttr('disabled');
        }
    });
});
