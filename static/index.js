function like(articleId) {
    const likeCount = document.getElementById(`likes-count-${articleId}`);
    const likeButton = document.getElementById(`like-button-${articleId}`);
  
    fetch(`/like-article/${articleId}`, { method: "POST" })
      .then((res) => res.json())
      .then((data) => {
        likeCount.innerHTML = data["likes"];
        if (data["liked"] === true) {
          likeButton.className = "fas fa-heart";
        } else {
          likeButton.className = "far fa-heart";
        }
      })
      .catch((e) => alert("Could not like article."));
  }