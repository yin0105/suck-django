function onSignIn(googleUser) {
    // console.log('------ this sithe onsign in -----')
    var profile = googleUser.getBasicProfile();
    // console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    // console.log('Name: ' + profile.getName());
    // console.log('Image URL: ' + profile.getImageUrl());
    // console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    let json_data = {
        social_type: 'google',
        social_id: profile.getId(),
        social_name: profile.getName(),
        social_email: profile.getEmail(),
        social_image: profile.getImageUrl()
    }
    let url_path = profile_update_url;
    $.post(url_path, json_data, moreResponse);
}
function onSuccess(googleUser) {
   var profile = googleUser.getBasicProfile();
    // console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    // console.log('Name: ' + profile.getName());
    // console.log('Image URL: ' + profile.getImageUrl());
    // console.log('Email: ' + profile.getEmail());
    let json_data = {
        social_type: 'google',
        social_id: profile.getId(),
        social_name: profile.getName(),
        social_email: profile.getEmail(),
        social_image: profile.getImageUrl()
    }
    let url_path = profile_update_url;
    $.post(url_path, json_data, moreResponse);    
}
function onFailure(error) {
    console.log(error);
}
function renderButton() {
    gapi.signin2.render('my-signin2', {
        'scope': 'profile email',
        'width': 240,
        'height': 50,
        'longtitle': true,
        'theme': 'dark',
        'onsuccess': onSuccess,
        'onfailure': onFailure
    });
}
function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
    console.log('User signed out.');
    });
}

function moreResponse(data, status) {
    console.log(data)
    if (data.status == 1) {
        $('#my-signin2').hide()
        $('#google-verify').empty()
        $('#google-verify').html('You were signed in through Google')
    }
}

function getData(data) {
    let json_data = {
        path: data
    };
    let url_path = profile_update_url;
    $.post(url_path, json_data, moreResponse);
}

$('#sign-out').click(function(){
    setTimeout(function() {
        signOut();
        window.location.href = '/logout'
    }, 3000)
})