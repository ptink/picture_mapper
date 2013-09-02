/**
 * Takes the URL of the model delete function, and sends a POST
 * request to delete after asking for confirmation.
 * @param url
 */
function deleteModel(url) {
    if (confirm("Are you sure you wish to delete?")) {
        $.ajax(url, {
            type: 'POST',
            success: function() { location.reload() },
            error: function() {
                alert("Delete failed.");
                location.reload();
            }
        });
    }
}
