function acceptProposal(proposalID) {
    var jqxhr = $.post( "127.0.0.1:5000/proposal", {type: 'accept',proposalID: proposalID}, function() {
        alert( "success" );
    })
        .done(function() {
            alert( "second success" );
        })
        .fail(function() {
            alert( "error" );
        })
        .always(function() {
            alert( "finished" );
        });
}

function rejectProposal(proposalID) {
    var jqxhr = $.post( "127.0.0.1:5000/proposal", {type: 'reject',proposalID: proposalID}, function() {
        alert( "success" );
    })
        .done(function() {
            alert( "second success" );
        })
        .fail(function() {
            alert( "error" );
        })
        .always(function() {
            alert( "finished" );
        });
}

$(document).ready(function () {

});
