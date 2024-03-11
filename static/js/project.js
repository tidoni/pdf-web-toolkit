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
    window.addEventListener('resize', () => this.scale_page_view());
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
    scale_page_view() {
      const overview_wrapper_width = document.getElementById('overview-wrapper').offsetWidth;
      // console.debug('width: ', overview_wrapper_width)

      const page_overview = document.getElementById('page_overview');

      const page_overview_height = `${overview_wrapper_width}px`;
      page_overview.style.height = page_overview_height;

      let page_overview_margin_bottom = '';
      if (!pdf_uploaded) {
        page_overview_margin_bottom = `${-1 * (overview_wrapper_width)}px`;
        page_overview.style.width = '0px';
      } else {
        page_overview_margin_bottom = `${-1 * (overview_wrapper_width - 500)}px`;
        page_overview.style.width = '500px';
      }
      console.debug('page_overview_margin_bottom: ', page_overview_margin_bottom);
      page_overview.style['margin-bottom'] = page_overview_margin_bottom;
      document.getElementById('overview-wrapper').style['border-bottom'] = '1px solid #fff';
    },
    display_pages() {
      const div_overview = document.getElementById('page_overview');
      div_overview.innerHTML = '';
      console.debug('div_overview', div_overview);

      fetch(`/get_single_pages_info/${uuid}/`, {
        method: 'GET',
      })
        .then((response) => response.json())
        .then((data) => {
          console.debug('data from Backend: ', data);
          if (data.status === 200) {
            document.getElementById('page_overview').style.width = '500px'; // Set initial width...
            this.scale_page_view();

            // eslint-disable-next-line no-restricted-syntax
            for (const page in data.pages) {
              if (data.pages[page] !== undefined) {
                console.debug(page);

                const node = document.createElement('embed');
                node.type = 'application/pdf';
                node.src = data.pages[page];
                node.classList.add('single_page_embed');

                const div_page = document.createElement('div');
                div_page.classList.add('single_page_div');
                div_page.appendChild(node);

                div_page.innerHTML += '<div class="btn-group pdf-interact-buttons" role="group" aria-label="page interact buttons" style="display: flex;">';
                div_page.innerHTML += `<button type="button" class="btn btn-outline-secondary" onclick="vueInstance.move_page(${Number(page) + 1}, ${Number(page)})"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-box-arrow-left" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0z"/><path fill-rule="evenodd" d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708z"/></svg></button>`;
                div_page.innerHTML += '<button hidden type="button" class="btn btn-outline-secondary"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16"><path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/><path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/></svg></button>';
                div_page.innerHTML += `<button type="button" class="btn btn-outline-secondary" onclick="vueInstance.move_page(${Number(page) + 1}, ${Number(page) + 2})"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-box-arrow-right" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0z"></path><path fill-rule="evenodd" d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708z"></path></svg></button>`;
                div_page.innerHTML += '</div>';

                // node.display = 'inline-block'
                div_overview.appendChild(div_page);
              }
            }
            console.debug(data.status);
          } else {
            console.debug(data.status);
            console.error('Project could not be created');
          }
        })
        .catch((error) => console.error(error));
      console.debug('div_overview', div_overview);
    },
    side_loaded() {
      document.getElementById('btn_download_complete').addEventListener('click', () => new pdf_api_wrapper(`${uuid}`).download_pdf());
      document.getElementById('btn_download_singel_pages').addEventListener('click', () => new pdf_api_wrapper(`${uuid}`).download_split_pdf());
      this.scale_page_view();

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
        this.display_pages();
        // eslint-disable-next-line no-undef
        bootstrap.Toast.getOrCreateInstance(document.getElementById('success-upload-toast')).show();
      });

      // eslint-disable-next-line no-unused-vars
      dropzone.on('error', (file, xhr, formData) => {
        // eslint-disable-next-line no-undef
        bootstrap.Toast.getOrCreateInstance(document.getElementById('warn-upload-toast')).show();
      });
    },
  },
});
