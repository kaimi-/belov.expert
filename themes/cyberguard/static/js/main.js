document.addEventListener('DOMContentLoaded', function() {
    // Publications toggle
    const viewToggle = document.querySelector('.view-toggle');
    if (viewToggle) {
        viewToggle.addEventListener('click', function(e) {
            e.preventDefault();
            const isShowingAll = this.getAttribute('data-showing-all') === 'true';
            const hiddenPublications = document.querySelectorAll('.hidden-publication');
            
            if (isShowingAll) {
                // Hide publications
                hiddenPublications.forEach(pub => {
                    pub.style.display = 'none';
                });
                this.setAttribute('data-showing-all', 'false');
                this.textContent = document.documentElement.lang === 'ru' ? 
                    'Показать все публикации' : 'View All Publications';
                
                // Scroll to publications section
                document.getElementById('publications').scrollIntoView({ behavior: 'smooth' });
            } else {
                // Show all publications
                hiddenPublications.forEach(pub => {
                    pub.style.display = 'block';
                });
                this.setAttribute('data-showing-all', 'true');
                this.textContent = document.documentElement.lang === 'ru' ? 
                    'Скрыть публикации' : 'Hide Publications';
            }
        });
    }

    // Add any other JavaScript functionality here
}); 