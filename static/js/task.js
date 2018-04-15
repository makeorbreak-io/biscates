function acceptProposal(proposalID) {
    hideInfoProposal

    var jqxhr = $.post( "/proposal", {type: 'accept',proposalID: proposalID}, function(result) {
    })
         .done(function() {
           showInfoProposal("A sua acção foi registada")
        })
        .fail(function(e) {
            showInfoProposal("Por favor, tente mais tarde")
        })
}

function rejectProposal(proposalID) {
    hideInfoProposal();
    var jqxhr = $.post( "/proposal", {type: 'reject',proposalID: proposalID}, function() {

    })
        .done(function() {
           showInfoProposal("A sua acção foi registada")
        })
        .fail(function(e) {
            showInfoProposal("Por favor, tente mais tarde")
        })

}

function showInfoProposal(msg) {
        $("#infoNewPropose").show();
        $("#infoNewProposemsg").text(msg)
}

function hideInfoProposal() {
        $("#infoNewPropose").hide();
}

$(document).ready(function () {

});
