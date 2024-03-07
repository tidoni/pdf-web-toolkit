/* eslint-disable camelcase */
/* eslint-disable no-console */

// eslint-disable-next-line no-unused-vars
class pdf_api_wrapper {
  constructor(project_uuid) {
    this.uuid = project_uuid;
  }

  downloadURI(uri, name) {
    const link = document.createElement('a');
    link.download = name;
    link.href = uri;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    // delete link;
  }

  download_pdf() {
    console.debug('download_pdf triggered');
    this.downloadURI(`/projects/${this.uuid}/complete.pdf`, 'complete_project.pdf');
  }

  download_split_pdf() {
    fetch(`/get_single_pages_archive/${this.uuid}/`, {
      method: 'GET',
    })
      .then((response) => response.json())
      .then((data) => {
        console.debug('data from Backend: ', data);
        if (data.status === 200) {
          this.downloadURI(`/projects/${this.uuid}/pdf_splitted.zip`, 'splitted_pdfs.zip');
          console.info('Archive with single Pages-PDFs created');
        } else {
          console.error('Project could not be created');
        }
      })
      .catch((error) => console.error(error));
  }
}
