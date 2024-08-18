// Javascript to edit reviews

document.addEventListener('DOMContentLoaded', () => {
    const editButtons = document.getElementsByClassName('btn-edit');
    const reviewText = document.getElementById('id_review_content');
    const reviewForm = document.getElementById('reviewForm');
    const submitButton = document.getElementById('submitButton');

    for (let button of editButtons) {
        button.addEventListener('click', (e) => {
            const reviewId = e.target.getAttribute('data-comment-id');
            const reviewTitle = e.target.closest('.card').querySelector('li:first-child').innerText.split(': ')[1];
            const reviewContent = e.target.closest('.card').querySelector('li:nth-child(2)').innerText.split(': ')[1];
            const reviewRating = e.target.closest('.card').querySelector('li:nth-child(4)').innerText.split(' / out of 5')[0].trim();

            reviewText.value = reviewContent;
            reviewForm.querySelector('input[name="review_title"]').value = reviewTitle;
            reviewForm.querySelector('textarea[name="review_content"]').value = reviewContent;

            const ratingSelect = reviewForm.querySelector('select[name="rating"]');
            if (ratingSelect) {
                console.log('Setting rating select value:', reviewRating);
                ratingSelect.value = reviewRating;
            } else {
                console.error('Rating select not found');
            }
            submitButton.innerText = 'Update';
            reviewForm.setAttribute('action', `edit_review/${reviewId}`);
        });
    }
});

// Javascript to Delete reviews

document.addEventListener('DOMContentLoaded', () => {
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let reviewId = e.target.getAttribute("data-comment-id");
            deleteConfirm.href = `delete_review/${reviewId}`;
            deleteModal.show();
        });
    }
});

