export async function getParametersSearchList(columns)
{
    let params = {};
    columns.forEach(x => {
        params[x.propName] = document.getElementById('search-bar-input-' + x.propName)?.value
    });

    return params;
}

export async function selectRow(user, index)
{
  console.log("Index clicado:", index)
  console.log("Usuário clicado:", user)
}