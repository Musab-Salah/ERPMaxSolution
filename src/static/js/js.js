function goBackOrRedirect() {
  if (document.referrer) {
    window.history.back();
  } else {
    window.location.href = "/";
  }
}

