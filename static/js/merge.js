/* eslint-disable new-cap */
/* eslint-disable camelcase */
/* eslint-disable no-console */

let uuid;
let pdf_uploaded = false;
import('./pdf_api_wrapper.js');

// eslint-disable-next-line no-undef, no-unused-vars
const vueInstance = new Vue({
  el: '#app',
  data() {
    return {
      pdf_file: null,
      project_uuid: null,
    };
  },
  mounted() {
    window.addEventListener('load', () => this.side_loaded());
  },
  methods: {
    move_page(from_page, to_page) {
      console.debug('trying to move page: ', from_page, to_page);
      fetch(`/move_page/${this.project_uuid}/${from_page}/${to_page}`, {
        method: 'GET',
      })
        .then((response) => response.json())
        .then((data) => {
          console.debug('data from Backend: ', data);
          if (data.status === 200) {
            this.display_pages();
            console.info('Page was moved');
          } else {
            console.error('Page could not be moved');
          }
        })
        .catch((error) => console.error(error));
    },
    side_loaded() {
      document.getElementById('btn_download_complete').addEventListener('click', () => new pdf_api_wrapper(`${uuid}`).download_pdf());

      fetch('/init_project/', {
        method: 'GET',
      })
        .then((response) => response.json())
        .then((data) => {
          console.debug('data from Backend: ', data);
          if (data.status === 200) {
            this.project_uuid = data.project_uuid;
            uuid = data.project_uuid;
          } else {
            this.project_uuid = null;
            console.error('Project could not be created');
          }
        })
        .catch((error) => console.error(error));

      // Dropzone has been added as a global variable.
      // eslint-disable-next-line no-undef
      const dropzone = new Dropzone('div#pdf-dropzone', {
        url: '/add_pdf_to_project/',
        paramName: 'pdf',
      });

      dropzone.on('addedfile', (file) => {
        console.log('A file has been added');
        // eslint-disable-next-line no-param-reassign
        file.previewElement.innerHTML = '';
        console.debug('Suppress file.previewElement');
        console.debug('PDF Project UUID: ', this.project_uuid);
      });

      dropzone.on('sending', (file, xhr, formData) => {
        formData.append('uuid', uuid);
      });

      // eslint-disable-next-line no-unused-vars
      dropzone.on('complete', (file, xhr, formData) => {
        pdf_uploaded = true;
        document.getElementById('btn-group-download').style.display = 'flex';
      });
    },
  },
});
